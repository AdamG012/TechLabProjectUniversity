import React from 'react'
import { Map as LeafletMap, TileLayer, Marker, Popup } from 'react-leaflet';

// Changed Map js to a React component
class Map extends React.Component {
    render() {
        return (
            <LeafletMap

                center={[-33.891710, 151.191510]}
                zoom={13}
                markerPosition={[-33.891710, 151.191510]}
                maxZoom={15}
                attributionControl={true}
                zoomControl={true}
                doubleClickZoom={true}
                scrollWheelZoom={true}
                dragging={true}
                easeLinearity={0.35}
            >
                <TileLayer
                    // Black and white leaflet wmflabs
                    url='http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png'
                />
                <Marker position={[-33.891710, 151.191510]}>
                    <Popup>
                        TechLab Sydney
                    </Popup>
                </Marker>
            </LeafletMap>
        );
    }
}

export default Map