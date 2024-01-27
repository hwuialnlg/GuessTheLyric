import HomeIcon from '@mui/icons-material/Home';
import TextField from '@mui/material/TextField';

function Gameplay(){
    return (
        <div className="">
            <GameplayNavBar/>


        </div>

    )
}

function GameplayNavBar(){
    let counter = 10;
    let lyric = "Trust Me Bro";
    return (
        <div className='gameplay-wrapper'>
            <div className='gameplay-navbar'>
                <div className='counter-icon'>
                    <p className='green'>{counter}</p>
                </div>
                <p className='green'>Guess The Lyric</p>
                <HomeIcon sx={{ fontSize: 70 }} className='home-icon white'/>
            </div>

            <div className='lyric-outer'>
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