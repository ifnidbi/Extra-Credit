async function requestJson(path, method = "GET", data = null) {
    const headers = {Accept: "application/json"};
    let body;
    if (method !== "GET") {
        headers["X-CSRFToken"] = document.querySelector('meta[name="csrf-token"]').content;
        if (data instanceof FormData) {
            body = data;
        } else if (data !== null) {
            headers["Content-Type"] = "application/json";
            body = JSON.stringify(data);
        }
    }

    let response;
    try {
        response = await fetch(path, {method, headers, body});
    } catch {
        throw new Error("Could not reach the server. Try again.");
    }
    if (response.status === 204) return null;

    const result = await response.json().catch(() => ({}));
    if (!response.ok) {
        const error = new Error(result.error?.message || `Request failed (${response.status}).`);
        error.fields = result.error?.fields;
        throw error;
    }
    return result.data;
}

function setMessage(element, message, failed = false) {
    if (element) {
        element.textContent = message;
        element.classList.toggle("error", failed);
    }
}

function addPhoto(photo) {
    const gallery = document.querySelector("#edit-photos");
    const card = document.createElement("div");
    card.dataset.photo = "";
    const image = document.createElement("img");
    image.src = photo.media_url;
    image.alt = "Listing photo";
    const form = document.createElement("form");
    form.dataset.apiForm = `/api/listings/${gallery.dataset.listing}/images/${photo.image_id}`;
    form.dataset.method = "DELETE";
    form.dataset.action = "delete-photo";
    const button = document.createElement("button");
    button.textContent = "Remove photo";
    const status = document.createElement("p");
    status.setAttribute("role", "status");
    status.dataset.message = "";
    form.append(button, status);
    card.append(image, form);
    gallery.append(card);
}

function addCategory(category) {
    const row = document.querySelector("#category-template").content.cloneNode(true);
    row.querySelector("input").value = category.category_name;
    for (const form of row.querySelectorAll("form")) {
        form.dataset.apiForm = `/api/categories/${category.category_id}`;
    }
    document.querySelector("#categories").append(row);
}

function updateInquiry(row, status) {
    row.querySelector("[data-state]").textContent = status;
    if (status !== "Pending") {
        for (const control of row.querySelectorAll("[data-pending]")) control.remove();
    }
}

function handleSuccess(form, result) {
    const action = form.dataset.action;
    const status = form.querySelector("[data-message]");
    setMessage(status, form.dataset.success || "Saved.");

    if (action === "listing") window.location.assign(`/listings/${result.listing_id}`);
    if (action === "sign-out" || action === "browse") window.location.assign("/listings");
    if (action === "clear") form.reset();
    if (action === "upload") {
        addPhoto(result);
        form.reset();
        setMessage(status, "Photo uploaded.");
    }
    if (action === "delete-photo") form.closest("[data-photo]").remove();
    if (action === "add-category") {
        addCategory(result);
        form.reset();
    }
    if (action === "delete-category") form.closest("[data-category]").remove();
    if (action === "sold" || action === "remove") {
        const row = form.closest("[data-listing-row]");
        row.querySelector("[data-state]").textContent = result?.listing_status || "Removed";
        for (const control of row.querySelectorAll("[data-active]")) control.remove();
        if (action === "remove") form.remove();
    }
    if (action === "edit-inquiry") {
        const row = form.closest("[data-inquiry-row]");
        row.querySelector("[data-pickup]").textContent =
            `${result.pickup_location} · ${result.preferred_date} · ${result.payment_method}`;
    }
    if (action === "withdraw" || action === "decision") {
        const row = form.closest("[data-inquiry-row]");
        const state = result?.inquiry_status || "Withdrawn";
        updateInquiry(row, state);
        if (state === "Accepted") {
            for (const other of document.querySelectorAll("[data-inquiry-row]")) {
                if (other !== row && other.dataset.listing === row.dataset.listing &&
                    other.querySelector("[data-state]").textContent === "Pending") {
                    updateInquiry(other, "Declined");
                }
            }
        }
    }
}

document.addEventListener("submit", async event => {
    const form = event.target.closest("[data-api-form]");
    if (!form) return;
    event.preventDefault();
    if (form.dataset.confirm && !window.confirm(form.dataset.confirm)) return;
    const status = form.querySelector("[data-message]");
    const fields = new FormData(form);
    if (event.submitter?.name) fields.set(event.submitter.name, event.submitter.value);
    const data = form.hasAttribute("data-file-form") ? fields : Object.fromEntries(fields);
    const buttons = form.querySelectorAll("button");
    for (const button of buttons) button.disabled = true;
    for (const input of form.querySelectorAll("input, select, textarea")) input.removeAttribute("aria-invalid");
    setMessage(status, "Saving…");
    try {
        const result = await requestJson(form.dataset.apiForm, form.dataset.method, data);
        handleSuccess(form, result);
    } catch (error) {
        setMessage(status, error.message, true);
        if (error.fields) {
            for (const field of Object.keys(error.fields)) {
                const input = form.elements.namedItem(field);
                if (input?.setAttribute) input.setAttribute("aria-invalid", "true");
            }
        }
    } finally {
        for (const button of buttons) button.disabled = false;
    }
});

function cell(row, value) {
    const column = row.insertCell();
    column.textContent = value;
    return column;
}

function emptyRow(table, columns, text) {
    const column = cell(table.insertRow(), text);
    column.colSpan = columns;
}

function setupSearch(form) {
    const table = document.querySelector("#listing-rows");
    const pages = document.querySelector("#listing-pages");
    const message = document.querySelector("#search-message");
    let latest = 0;

    async function search(page) {
        const current = ++latest;
        const params = new URLSearchParams(new FormData(form));
        if (page > 1) params.set("page", page);
        setMessage(message, "Searching…");
        try {
            const result = await requestJson(`/api/listings?${params}`);
            if (current !== latest) return;
            table.replaceChildren();
            for (const item of result.items) {
                const row = table.insertRow();
                const link = document.createElement("a");
                link.href = `/listings/${item.listing_id}`;
                link.textContent = item.title;
                row.insertCell().append(link);
                cell(row, `${item.price} ${item.currency_code}`);
                cell(row, item.item_condition);
                cell(row, item.category_name);
                cell(row, item.campus_name);
            }
            if (!result.items.length) emptyRow(table, 5, "No listings found.");

            pages.replaceChildren();
            if (result.page > 1) pages.append(pageLink("Previous", result.page - 1, params));
            const pageText = document.createElement("span");
            pageText.textContent = `Page ${result.page}`;
            pages.append(pageText);
            if (result.has_next) pages.append(pageLink("Next", result.page + 1, params));
            window.history.replaceState(null, "", `/listings?${params}`);
            const noun = result.items.length === 1 ? "listing" : "listings";
            setMessage(message, `${result.items.length} ${noun} shown.`);
        } catch (error) {
            if (current === latest) setMessage(message, error.message, true);
        }
    }

    form.addEventListener("submit", event => {
        event.preventDefault();
        search(1);
    });
    pages.addEventListener("click", event => {
        const link = event.target.closest("a[data-page]");
        if (!link || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
        event.preventDefault();
        search(Number(link.dataset.page));
    });
}

function pageLink(label, page, params) {
    const link = document.createElement("a");
    const query = new URLSearchParams(params);
    query.set("page", page);
    link.href = `/listings?${query}`;
    link.dataset.page = page;
    link.textContent = label;
    return link;
}

async function setupChart(canvas) {
    const message = document.querySelector("#chart-message");
    try {
        const totals = await requestJson("/api/reports/category-counts");
        if (!totals.length) {
            setMessage(message, "No category totals to chart.");
            return;
        }
        new Chart(canvas, {
            type: "bar",
            data: {
                labels: totals.map(row => row.category_name),
                datasets: [{label: "Listings", data: totals.map(row => row.listing_count), backgroundColor: "#4381b1"}]
            },
            options: {animation: false, scales: {y: {beginAtZero: true, ticks: {precision: 0}}}}
        });
    } catch {
        setMessage(message, "Could not load the chart. The category table is below.", true);
    }
}

function setupWeather(search) {
    const save = document.querySelector("#weather-save");
    const menu = save.elements.place;
    const table = document.querySelector("#weather-rows");
    const message = document.querySelector("#weather-message");
    let places = [];
    let latest = 0;

    async function readHistory() {
        const forecasts = await requestJson("/api/weather/snapshots");
        table.replaceChildren();
        for (const forecast of forecasts) {
            const row = table.insertRow();
            cell(row, forecast.place_label);
            cell(row, forecast.forecast_date);
            cell(row, `${forecast.max_temp_c} °C`);
            cell(row, `${forecast.precip_probability}%`);
        }
        if (!forecasts.length) emptyRow(table, 4, "No forecasts saved yet.");
    }

    search.addEventListener("submit", async event => {
        event.preventDefault();
        const current = ++latest;
        const params = new URLSearchParams(new FormData(search));
        save.hidden = true;
        setMessage(message, "Finding cities…");
        try {
            const result = await requestJson(`/api/weather/places?${params}`);
            if (current !== latest) return;
            places = result;
            menu.replaceChildren();
            for (const [index, place] of places.entries()) menu.add(new Option(place.place_label, index));
            if (places.length) save.hidden = false;
            setMessage(message, places.length ? "Choose a city." : "No cities found.");
        } catch (error) {
            if (current === latest) setMessage(message, error.message, true);
        }
    });

    save.addEventListener("submit", async event => {
        event.preventDefault();
        const place = places[Number(menu.value)];
        if (!place) return;
        const button = save.querySelector("button");
        button.disabled = true;
        setMessage(message, "Getting forecast…");
        try {
            await requestJson("/api/weather/snapshots", "POST", place);
            setMessage(message, "Forecast saved.");
            try {
                await readHistory();
            } catch (error) {
                setMessage(message, "Forecast saved. Reload to see the updated history.", true);
            }
        } catch (error) {
            setMessage(message, error.message, true);
        } finally {
            button.disabled = false;
        }
    });

    readHistory().catch(error => setMessage(message, error.message, true));
}

const search = document.querySelector("#search");
const chart = document.querySelector("#category-chart");
const weather = document.querySelector("#weather-search");

if (search) setupSearch(search);
if (chart) setupChart(chart);
if (weather) setupWeather(weather);
