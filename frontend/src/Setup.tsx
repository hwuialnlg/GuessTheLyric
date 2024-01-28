import Navbar from "./components/Navbar";
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import { useState } from "react";
import axios from 'axios';
import { Link } from 'react-router-dom';

function Setup(){
    const [artists, setArtists] = useState("");
    const [maxSongs, setMaxSongs] = useState("6");
    const [lyricData, setLyricData] = useState("");

    const handleArtists = (e: any) => {
        setArtists(e.target.value);
      };
    
      const handleMaxSongs = (e: any) => {
        setMaxSongs(e.target.value);
      };

    const handleSetUp = async () => {
        let artistArray = artists.split("\n");

        try {
            const response = await axios.post('http://127.0.0.1:5000/lyrics', { message: [artistArray, maxSongs]});
            let serverResponse = response.data.response;
            setLyricData(serverResponse);
            

          } catch (error) {
            console.error("Error getting server response: ", error);
          }
    }

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
                    defaultValue={maxSongs}
                    InputLabelProps={{
                        shrink: true,
                    }}
                    onChange={handleMaxSongs}
                    />
                </div>

                <div className="setup-button-group">
                    {/* https://stackoverflow.com/a/71375996/21989952 */}
                    <Link to={`/play`} state={{lyricData}}>
                        <Button variant="contained"color="success" size="large" onClick={handleSetUp}>
                        Play
                        </Button>
                    </Link>                

                    <Link to="/home"> 
                        <Button variant="contained" size="large" color="error">
                        Quit
                        </Button>
                    </Link>                


                </div>
        </div>
        </div>
    )
}

export default Setup;