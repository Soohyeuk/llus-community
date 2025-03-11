import {useNavigate} from "react-router-dom"

function Home(){
    const navigate = useNavigate(); 
    return(
        <div>
            <h1>뉴욕대 웹사임</h1>
            <button onClick={() => navigate("/login")}>동료라면 로그인해라</button>  {/* Navigates to Login */}
            <button onClick={() => navigate("/signup")}>동료가 되고싶나?</button>  
        </div>
    );
}
export default Home;