import React from 'react'
import { Map as LeafletMap, TileLayer, Marker, Popup } from 'react-leaflet';

// Changed Map js to a React component
class Map extends React.Component {
    render() {
        return (
            <LeafletMap
                center={[50, 10]}
                zoom={6}
                maxZoom={10}
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
                <Marker position={[50, 10]}>
                    <Popup>
                        Popup for any custom information.
                    </Popup>
                </Marker>
            </LeafletMap>
        );
    }
}

export default Map