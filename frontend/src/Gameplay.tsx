import HomeIcon from '@mui/icons-material/Home';
import TextField from '@mui/material/TextField';
import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { useLocation } from 'react-router-dom'

function Gameplay(){
    return (
        <div className="">
            <GameplayNavBar/>


        </div>

    )
}

function GameplayNavBar(){
    const {state} = useLocation();
    let lyricsArray = null;

    if (state != null){
        const {lyrics} = state;
        lyricsArray =lyrics.serverResponse;
    }

    const randomElement = lyricsArray[Math.floor(Math.random() * lyricsArray.length)]; //picking random ele from array

    const [score, setScore] = useState(0);
    const [artist, setArtist] = useState(randomElement[0]);
    const [song, setSong] = useState(randomElement[1]);
    const [lyric, setLyric] = useState(randomElement[2].slice(0, randomElement[3][0]));
    // let lyric = "Trust Me Bro";
  

    // https://stackoverflow.com/a/4550514/21989952    

    return (
        <div className='gameplay-wrapper'>
            <div className='gameplay-navbar'>
                <Counter lyricsArray={lyricsArray} setSong={setSong} setArtist={setArtist} setLyric={setLyric}/>
                <p className='green'>Guess The Lyric</p>
                <Link to="/home"><HomeIcon sx={{ fontSize: 70 }} className='home-icon white'/></Link>                
                
            </div>

            <div className='lyric-outer'>

                <div className='test'>
                    <div className="lyric-left-side">
                        <img className="lyric-artist-image" src=""></img>
                        <p className="lyric-score">score: {score}</p>
                        <p className="lyric-artist-song">{artist} - {song}</p>
                    </div>
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

const Counter = (props: any) => {
    const [counter, setCounter] = useState(10);

    useEffect(() => {
        
        const interval = setInterval(() => {
            setCounter(counter - 1);
        }, 1000);

        return () => 
        clearInterval(interval);
        
    }, [counter]);

    if (counter === 0) {
        const randomElement = props.lyricsArray[Math.floor(Math.random() * props.lyricsArray.length)]; //picking random ele from array
        props.setArtist(randomElement[0]);
        props.setSong(randomElement[1]);
        props.setLyric(randomElement[2]);
        setCounter(10);
      }

    return (
        <div className='counter-icon'>
        {/* https://stackoverflow.com/a/51915955/21989952 */}
        {counter <= 3 ? <p className='red'>{counter > 0 ? (counter < 10 ? "0" + counter : counter) : "00"}</p> : <p className='green'>{counter > 0 ? (counter < 10 ? "0" + counter : counter) : "00"}</p>}
        </div>
    )
}

export default Gameplay;