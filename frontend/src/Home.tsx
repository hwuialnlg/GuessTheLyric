import Navbar from "./components/Navbar";

function Home(){
    // const options = ["Play, Leaderboards, About"];
    return (
        <div className="home-wrapper">
            <Navbar/>

            <div className="menu-items">
                <div className="menu-option">
                    <p>Play</p>
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