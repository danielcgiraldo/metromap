const modal = document.getElementById("station_info");

function reset_modal() {
    modal.innerHTML = `<header>
        <div class="title">
            <button class="close">x</button>
        </div>
        <div class="map">
            <div class="block skeleton"></div>
        </div>
    </header>
    <div class="info">
        <div class="line skeleton" style="width: 60%; margin: 2vw 0 1vw 0;"></div>
        <div class="line skeleton" style="margin-bottom: 1vw;"></div>
        <div class="line skeleton" style="margin-bottom: 2vw;"></div>
    </div>`
}

function close_modal() {
    modal.querySelector("button.close").addEventListener("click", () => {
        modal.classList.remove("active")
        reset_modal()
    })
}

async function focus_station(ev) {



    /* data */
    const station = ev.target;
    const idStation = station.classList[0];
    const lineParent = station.parentNode;
    const line = lineParent.classList[0];
    const idLine = (line.match(/linea([a-zA-Z0-9])/g)[0].slice(-1));

    reset_modal()

    /* modal */
    modal.classList.add("active")
    const infoSection = modal.querySelector(".info");

    fetch(`https://embed.metromap.online/request?uri=https://api.metromap.online/v1/data/${idLine}/${idStation}`)
        .then(response => response.json())
        .then(data => {
            infoSection.innerHTML = ``
            // Guarda la respuesta en una variable
            if (data.status == "ok") {
                console.log(data.data[idLine][idStation].sites_of_interest)
                const stationSitesOfInterest = data.data[idLine][idStation].sites_of_interest;
                const stationServices = data.data[idLine][idStation].services;
                const stationName = data.data[idLine][idStation].name;
                const lineColor = data.data[idLine]["color"];
                modal.querySelector("header .title").innerHTML = `<h3>${stationName}</h3>
                    <div class="line" style="--line-color: #${lineColor}" >${idLine}</div>
                    <button class="close">x</button>`;
                modal.querySelector("header .map").innerHTML = `<iframe width="100%" height="100%" id="gmap_canvas"
                src="https://maps.google.com/maps?q=Estación ${stationName} Línea ${idLine}&t=&z=17&ie=UTF8&iwloc=&output=embed"
                frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>`;
                close_modal()

                if (stationServices != "NULL") {

                    let stationServicesResult = "";
                    stationServicesResult += `<div class="title">
                        <h4>Servicios</h4>
                        <span> / Services</span>
                    </div>
                    <div class="group">`;
                    if (stationServices.includes("PAC")) {
                        stationServicesResult += `<div class="row">
                        <img src="https://metromapmed.s3.amazonaws.com/assets/img/icons/pac.jpg" alt="Punto de Atención">
                        <h6>Punto de Atención al Cliente</h6>
                        <span>/ Customer Service Point</span>
                        </div>`
                    }
                    if (stationServices.includes("ruta_integrada")) {
                        stationServicesResult += `<div class="row">
                        <img src="https://metromapmed.s3.amazonaws.com/assets/img/icons/ruta_integrada.jpg" alt="Ruta Integrada">
                        <h6>Ruta Integrada</h6>
                        <span>/ integrated route</span>
                        </div>`
                    }
                    if (stationServices.includes("parqueadero_para_bicicletas")) {
                        stationServicesResult += `<div class="row">
                        <img src="https://metromapmed.s3.amazonaws.com/assets/img/icons/parqueadero_para_bicicletas.jpg" alt="parqueadero_para_bicicletas">
                        <h6>Parqueadero para Bicicletas</h6>
                        <span>/ Bicycle Parking</span>
                        </div>`
                    }
                    if (stationServices.includes("bibliometro")) {
                        stationServicesResult += `<div class="row">
                        <img src="https://metromapmed.s3.amazonaws.com/assets/img/icons/bibliometro.jpg" alt="bibliometro">
                        <h6>Bibliometro</h6>
                        <span>/ Library</span>
                        </div>`
                    }
                    if (stationServices.includes("sala_de_alfabetizacion_digital")) {
                        stationServicesResult += `<div class="row">
                        <img src="https://metromapmed.s3.amazonaws.com/assets/img/icons/sala_de_alfabetizacion_digital.jpg" alt="sala_de_alfabetizacion_digital">
                        <h6>Sala de Alfabetizacion Digital</h6>
                        <span>/ Digital Literasy Room</span>
                        </div>`
                    }
                    if (stationServices.includes("zona_wifi")) {
                        stationServicesResult += `<div class="row">
                        <img src="https://metromapmed.s3.amazonaws.com/assets/img/icons/zona_wifi.jpg" alt="zona_wifi">
                        <h6>Zona WIFI</h6>
                        <span>/ WiFi Zone</span>
                        </div>`
                    }
                    if (stationServices.includes("estacion_encicla")) {
                        stationServicesResult += `<div class="row">
                        <img src="https://metromapmed.s3.amazonaws.com/assets/img/icons/estacion_encicla.jpg" alt="estacion_encicla">
                        <h6>Estación EnCicla</h6>
                        <span>/ EnCicla Station</span>
                        </div>`
                    }
                    stationServicesResult += `</div>`;
                    infoSection.innerHTML += stationServicesResult;
                    infoSection.classList.add("content")
                }
                if (stationSitesOfInterest != "NULL") {
                    let stationSitesOfInterestResult = "";
                    stationSitesOfInterestResult += `<div class="title">
                    <h4>Sitios de interés</h4>
                    <span> / Sites of interest</span>
                    </div>
                    <div class="group">`;
                    const sites = stationSitesOfInterest.replace(/[{}"]/g, "").split(",");
                    for (let i = 0; i < sites.length; i++) {
                        stationSitesOfInterestResult += `<div class="row">
                                <a href="https://maps.google.com/maps?q=${sites[i]}, Medellín" target="_blank">
                        <h6>${sites[i]}</h6>
                        </a>
                        </div>`
                    }
                    stationSitesOfInterestResult += `</div>`;
                    infoSection.innerHTML += stationSitesOfInterestResult;
                    infoSection.classList.add("content")
                }
            } else {
                modal.classList.remove("active")
            }

            fetch(`https://embed.metromap.online/request?uri=https://api.metromap.online/v1/incident/${idLine}/${idStation}`)
                .then(response => response.json())
                .then(data => {
                    // Guarda la respuesta en una variable
                    if (data.status == "ok") {
                        if (data.data[idLine] && data.data[idLine][idStation]) {
                            if (data.data[idLine][idStation].status == "P") {
                                modal.querySelector(".info").insertAdjacentHTML("afterbegin", `<a class="alert ${stationStatus}" href="https://twitter.com/metrodemedellin/status/${data.data[idLine][idStation].tweet_id}" target="_blank">
                            <svg width="649" height="573" viewBox="0 0 649 573" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" clip-rule="evenodd"
                                    d="M375.04 29.0626C364.587 11.1453 345.409 0.130615 324.665 0.130615C303.921 0.130615 284.744 11.1462 274.291 29.0626L8.54397 484.596C-1.98203 502.659 -2.04976 524.94 8.35648 543.049C18.7627 561.153 38.0391 572.331 58.9445 572.331H590.385C611.291 572.331 630.567 561.154 640.972 543.049C651.379 524.94 651.311 502.659 640.785 484.596L375.04 29.0626ZM324.665 420.663C340.764 420.663 353.832 433.73 353.832 449.829C353.832 465.928 340.764 478.996 324.665 478.996C308.566 478.996 295.499 465.928 295.499 449.829C295.499 433.73 308.566 420.663 324.665 420.663ZM301.332 198.996V362.329C301.332 375.21 311.785 385.663 324.665 385.663C337.546 385.663 347.999 375.21 347.999 362.329V198.996C347.999 186.116 337.546 175.663 324.665 175.663C311.785 175.663 301.332 186.116 301.332 198.996Z"
                                    fill="black" />
                            </svg>
                            Parcialmente Operativa
                        </a>`)
                            } else if (data.data[idLine][idStation].status == "M") {
                                modal.querySelector(".info").insertAdjacentHTML("afterbegin", `<a class="alert ${stationStatus}" href="https://twitter.com/metrodemedellin/status/${data.data[idLine][idStation].tweet_id}" target="_blank">
                            <svg width="649" height="573" viewBox="0 0 649 573" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" clip-rule="evenodd"
                                    d="M375.04 29.0626C364.587 11.1453 345.409 0.130615 324.665 0.130615C303.921 0.130615 284.744 11.1462 274.291 29.0626L8.54397 484.596C-1.98203 502.659 -2.04976 524.94 8.35648 543.049C18.7627 561.153 38.0391 572.331 58.9445 572.331H590.385C611.291 572.331 630.567 561.154 640.972 543.049C651.379 524.94 651.311 502.659 640.785 484.596L375.04 29.0626ZM324.665 420.663C340.764 420.663 353.832 433.73 353.832 449.829C353.832 465.928 340.764 478.996 324.665 478.996C308.566 478.996 295.499 465.928 295.499 449.829C295.499 433.73 308.566 420.663 324.665 420.663ZM301.332 198.996V362.329C301.332 375.21 311.785 385.663 324.665 385.663C337.546 385.663 347.999 375.21 347.999 362.329V198.996C347.999 186.116 337.546 175.663 324.665 175.663C311.785 175.663 301.332 186.116 301.332 198.996Z"
                                    fill="black" />
                            </svg>
                            Fuera de Servicio
                        </a>`)

                            }
                        }
                    }
                })
                .catch(error => console.error(error));

        })
        .catch(error => () => { console.error(error); modal.classList.remove("active") });

    close_modal()
}

// Select all elements that have a class that constains the word "station"
const stations = document.querySelectorAll('.station');

// Add a "click" event to each element
stations.forEach(station => {
    station.addEventListener("click", focus_station);
});