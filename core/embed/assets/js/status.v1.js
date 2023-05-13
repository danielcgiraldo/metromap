function setup_status() {
    // Get initial status of all the stations and segments
    // Display the status of the stations
    fetch('https://embed.metromap.online/request?uri=https://api.metromap.online/v1/status')
        .then(response => response.json())
        .then(data => {
            if (data.status === 'ok') {
                const lines = Object.keys(data.data);
                for (let line of lines) {
                    if (data.data[line].status !== 'O') {
                        const stations = Object.keys(data.data[line].stations);
                        for (let i = 0; i < stations.length; i++) {
                            let status = data.data[line].stations[stations[i]].status;
                            station_status(line, stations[i], status);
                            if (i < stations.length - 1) {
                                segment_status(line, stations[i], stations[i + 1], status);
                            }
                        }
                    }
                }
            }
        })
        .catch(error => console.error(error));
}



// Select station
function station_status(line, station, status) {
    const linea = document.querySelector(`.linea${line}stations`);
    var estacion = linea.querySelector(`.${station}.station`);
    if (estacion === null) return;
    estacion.classList.remove("O", "M", "P", "U")
    estacion.classList.add(status);
}

// Select Segment
function segment_status(line, station1, station2, status) {
    if (status != "O") status = "M"
    const linea = document.querySelector(`.linea${line}segments`);
    if (linea === null) return;
    var segment = linea.querySelector(`.${station1}.${station2}`);
    if (segment === null) return;
    segment.classList.remove("O", "M")
    segment.classList.add(status);
}

setInterval(function minutero(line, station) {
    const fechaActual = new Date();
    fechaActual.setMinutes(fechaActual.getMinutes() - 6);
    const fechaMenos6Min = fechaActual.toISOString();

    fetch(`https://embed.metromap.online/request?uri=https://api.metromap.online/v1/incident/${line}/${station}?dt=${fechaMenos6Min}`)
        .then(response => response.json())
        .then(data => {
            if (data.status == "ok") {
                const lines = Object.keys(data.data);
                for (let line of lines) {
                    const stations = Object.keys(data.data[line].stations);
                    for (let i = 0; i < stations.length; i++) {
                        let status = data.data[line].stations[stations[i]].status;
                        station_status(line, stations[i], status);
                        if (i < stations.length - 1) {
                            segment_status(line, stations[i], stations[i + 1], status);
                        }
                    }
                }
            }
        })
        .catch(error => console.error(error));
}, 60000);

setup_status();