import {useNavigate} from "react-router-dom"
function Login() {
    const navigate = useNavigate();
    return (
      <div>
        <h2>로그인 페이지</h2>
        <button onClick={() => navigate("/signup")}>회원가입을 하지 않았더라면?</button>  
        </div>
      
    );
  }
  
  export default Login;  
  