import HomeIcon from '@mui/icons-material/Home';
import TextField from '@mui/material/TextField';
import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

function Gameplay(){
    return (
        <div className="">
            <GameplayNavBar/>


        </div>

    )
}

function GameplayNavBar(){
    
    const [counter, setCounter] = useState(10);
    const [score, setScore] = useState(0);
    const [artist, setArtist] = useState("temp artist");
    const [song, setSong] = useState("temp song");

    let lyric = "Trust Me Bro";

    useEffect(() => {
        const interval = setInterval(() => {
            setCounter(counter - 1);
        }, 1000);

        return () => clearInterval(interval);
    }, [counter]);

    if (counter === 0) {
        setCounter(10);
      }

    return (
        <div className='gameplay-wrapper'>
            <div className='gameplay-navbar'>
                <div className='counter-icon'>
                    {/* https://stackoverflow.com/a/51915955/21989952 */}
                    <p className='green'>{counter > 0 ? (counter < 10 ? "0" + counter : counter) : "00"}</p>
                </div>
                <p className='green'>Guess The Lyric</p>
                <Link to="/home"><HomeIcon sx={{ fontSize: 70 }} className='home-icon white'/></Link>                
                
            </div>

            <div className='lyric-outer'>

                <div className="lyric-left-side">
                    <img className="lyric-artist-image" src=""></img>
                    <p className="lyric-score">{score}</p>
                    <p className="lyric-artist-song">{artist} - {song}</p>
                </div>


                <div className='lyric-wrapper'>
                    <p>{lyric}</p>

                    <TextField
                        id="standard-search"
                        label=""
                        type="search"
                        variant="standard"
                    />

                </div>
            </div>
        </div>
    )
}

export default Gameplay;