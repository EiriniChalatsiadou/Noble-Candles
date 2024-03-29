/* jshint esversion: 6 */
/* globals $:false */

if (window.location.pathname == "/") {
    //initialise map
    const initMap = () => {
        // The location of Uluru
        const uluru = { lat: 53.3498, lng: -6.2603 };
        // The map, centered at Uluru
        const map = new google.maps.Map(document.getElementById("map"), {
            zoom: 4,
            center: uluru,
        });
        // The marker, positioned at Uluru
        new google.maps.Marker({
            position: uluru,
            map: map,
        });
    };
    initMap();
}
$('a.navbar-custom-collapse').click(function () {
    $("#navbarNav").collapse('hide');
});
