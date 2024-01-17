window.onload = init;

function init() {

    const mapElement = document.getElementById('mapid');

    const stadiaMap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'    
    })

    const stadiaMap2 = L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png',
     {
        maxZoom: 20,
        attribution: '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a> contributors'
     })
    const mymap = L.map(mapElement, {
        center: [51.505, -0.09],
        zoom: 13,
        minZoom: 7,
        zoomSnap: 0.25,
        zoomDelta: 0.25,
        layers: [stadiaMap
        ]
    })

    const baseMaps = {
        "OpenStreetMap": stadiaMap,
        "Stadia Maps": stadiaMap2
    }

    L.control.layers(baseMaps,{},
        {
        collapsed:true,
        position: 'bottomleft'
    }
    ).addTo(mymap);

    mymap.on('click', function(e){
        console.log(e)
    })

    // Perth marker
    const marker = L.marker([51.513336399623476, -0.09475708007812501],{
        title: 'Marker Exemplo',
        opacity: 0.7}
        ).addTo(mymap);

    // Popup

    const popup = L.popup({
        closeButton: false,
        closeOnClick: false,
        autoClose: false,
        className: 'my-popup',
        alt: 'Popup Exemplo',
        content: '<h2>Popup Exemplo</h2>'
    })

    marker.bindPopup(popup);
    
}