import Navbar from "./components/Navbar";
import { Link } from 'react-router-dom';

function Home(){
    // const options = ["Play, Leaderboards, About"];
    return (
        <div className="home-wrapper">
            <Navbar/>

            <div className="menu-items">
                <div className="menu-option">
                    
                <Link to="/play" style={{ color: 'inherit', textDecoration: 'inherit'}}><p>Play</p></Link>                
                </div>

                <div className="menu-option">
                    <p>Leaderboards</p>
                </div>
                
                <div className="menu-option">
                    <p>About</p>
                </div>
            </div>
        </div>

    )
}

export default Home;