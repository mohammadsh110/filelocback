import logo from './logo.svg';
import './App.css';
import DropImage from './dropzone';
import { useEffect, useState } from 'react';
const App = () => {

  let [lat,setLat]=useState(0.0);
  let [lon,setLon]=useState(0.0);

  useEffect(() => {
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(function (position) {
        try {
          setLat(position.coords.latitude)
          console.log("Latitude is :", position.coords.latitude);
          console.log("Longitude is :", position.coords.longitude);
          setLon(position.coords.longitude)
        } catch (err) {
          console.log(err);
        }

      });
    } else {
      console.log("Not Available");
    }
  });

  return (
    <div className="App">
      <div className="App">
        <DropImage lat={lat} lon={lon}/>
      </div>

    </div>
  )
}

export default App;
