import Navbar from "./components/Navbar";
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import { useState } from "react";

function Setup(){
    const [artists, setArtists] = useState("");
    const [maxSongs, setMaxSongs] = useState("");

    const handleArtists = (e) => {
        setArtists(e.target.value);
      };
    
      const handleMaxSongs = (e) => {
        setMaxSongs(e.target.value);
      };

    return (

        <div className="set-up-wrapper">
            <Navbar/>
            <div className="set-up-content">
                <div className="set-up-artist-box">
                    <p>Instructions: For the artists input, you can add 1 to 5 artist names. Seperate each artist with each line. Also, enter the max number of songs you would like to get from each artist. </p>
                </div>
                <div className="input-box">
                    <TextField
                    id="standard-textarea"
                    label="Artists"
                    placeholder="Placeholder"
                    multiline
                    variant="standard"
                    onChange={handleArtists}
                    />

                    <TextField
                    id="outlined-number"
                    label="Max Number of Songs"
                    type="number"
                    defaultValue="6"
                    InputLabelProps={{
                        shrink: true,
                    }}
                    onChange={handleMaxSongs}
                    />
                </div>

                <div className="setup-button-group">
                    <Button variant="contained"color="success" size="large">
                    Play
                    </Button>

                    <Button variant="contained" size="large" color="error">
                    Quit
                    </Button>
                </div>
        </div>
        </div>
    )
}

export default Setup;