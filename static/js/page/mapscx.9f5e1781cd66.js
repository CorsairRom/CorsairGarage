var geocoder;
var map;

function initialize() {
    geocoder = new google.maps.Geocoder();
    geocoder.geocode({ 'address': "los muermos 8122, hualpen" }, function (results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
            var mapOptions = {
                zoom: 15,
                center: new google.maps.LatLng(-36.788799, -73.090988),
                mapTypeId: google.maps.MapTypeId.ROADMAP
            }

            // Let's draw the map
            map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);

        }
        else {
            alert("Geocode was not successful for the following reason: " + status);
        }
    });
}

