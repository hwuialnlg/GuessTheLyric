import HomeIcon from '@mui/icons-material/Home';
import CircleIcon from '@mui/icons-material/Circle';

function Gameplay(){
    return (
        <div className="home-wrapper">
            <GameplayNavBar/>


        </div>

    )
}

function GameplayNavBar(){
    let counter = 0;
    return (
        <div className='gameplay-navbar'>
            <div className='counter-icon'>
                <div className='counter-wrapper'>
                    <CircleIcon sx={{ fontSize: 70 }} className='white'/>
                </div>
                <div className='counter-wrapper'>
                    <p className='green'>{counter}</p>
                </div>
            </div>
            <p className='green'>Guess The Lyric</p>
            <HomeIcon sx={{ fontSize: 70 }} className='home-icon white'/>

        </div>
    )
}

export default Gameplay;