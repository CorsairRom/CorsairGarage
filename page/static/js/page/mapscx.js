

function initMap() {
    const myLatLng = { lat: -36.7889240, lng: -73.08891  };
    const map = new google.maps.Map(document.getElementById("map"), {
        center: myLatLng,
        zoom: 16,
    });
    new google.maps.Marker({
        position: myLatLng,
        map,
        title: "Corsair Garage",
    });
    
}

window.initMap = initMap;
