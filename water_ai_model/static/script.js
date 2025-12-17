const CHANNEL_ID = "3164471";
const READ_API = "X699HIR4ZQX4IRHJ";
const TS_URL = `https://api.thingspeak.com/channels/${CHANNEL_ID}/feeds.json?api_key=${READ_API}&results=20`;

const phEl = document.getElementById("phValue");
const tdsEl = document.getElementById("tdsValue");
const turbEl = document.getElementById("turbidityValue");
const tempEl = document.getElementById("tempValue");
const badge = document.getElementById("statusBadge");

let chart;

// Fetch historical graph
async function loadHistory() {
    try {
        const res = await fetch(TS_URL);
        const data = await res.json();
        const feeds = data.feeds.reverse();

        const labels = feeds.map((f, i) => i + 1);

        const ph = feeds.map(f => parseFloat(f.field1 || 0));
        const tds = feeds.map(f => parseFloat(f.field3 || 0));
        const turb = feeds.map(f => parseFloat(f.field2 || 0));
        const temp = feeds.map(f => parseFloat(f.field4 || 0));

        const ctx = document.getElementById("historyChart").getContext("2d");

        if (!chart) {
            chart = new Chart(ctx, {
                type: "line",
                data: {
                    labels: labels,
                    datasets: [
                        { label: "pH", data: ph, borderColor: "skyblue", fill: false },
                        { label: "TDS", data: tds, borderColor: "pink", fill: false },
                        { label: "Turbidity", data: turb, borderColor: "orange", fill: false },
                        { label: "Temp", data: temp, borderColor: "gold", fill: false }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });
        } else {
            chart.data.labels = labels;
            chart.data.datasets[0].data = ph;
            chart.data.datasets[1].data = tds;
            chart.data.datasets[2].data = turb;
            chart.data.datasets[3].data = temp;
            chart.update();
        }
    } catch (e) {
        console.log("History error:", e);
    }
}

// Fetch /api/predict (AI + live values)
async function loadLatest() {
    try {
        const res = await fetch("/api/predict");
        const data = await res.json();

        if (!data.success) return;

        phEl.textContent = data.values.pH;
        tdsEl.textContent = data.values.TDS;
        turbEl.textContent = data.values.Turbidity;
        tempEl.textContent = data.values.Temperature;

        if (data.prediction === "SAFE") {
            badge.textContent = "SAFE";
            badge.className = "badge safe";
        } else {
            badge.textContent = "UNSAFE";
            badge.className = "badge unsafe";
        }
    } catch (e) {
        console.log("Predict error:", e);
    }
}

async function run() {
    await loadHistory();
    await loadLatest();
    document.getElementById("loading").style.display = "none";
}

run();
setInterval(run, 15000);
