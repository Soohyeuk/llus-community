import { BrowserRouter as Router, Route, Routes, useNavigate } from "react-router-dom";
import Signup from "./Signup";
import Login from "./Login";
import Profile from "./Profile";
/* 각각 싸인업 로그인 프로필에 있는걸로 임포트함 */

function Home() {/* 메인 페이지를 구성 */

  const navigate = useNavigate(); /* 버틀 클릭씨 router대로 가게 해줌 */

  return (
    <div>
      <h1>Welcome to Our App</h1>
      <button onClick={() => navigate("/signup")}>우리 동료가 되어라</button>
      <button onClick={() => navigate("/login")}>계정 만들었으면 로그인 ㄱ</button>
      <button onClick={() => navigate("/profile/1")}>내 프로필 ㄱ</button> 
    </div>

  );
}
/*router는 경로를 알려주는 지도 */
function App() {
  return (
    <Router> 
      <h1>뉴욕대 학교앱이라능</h1> 
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="/profile/:id" element={<Profile />} />
      </Routes>
    </Router>
  );
}

export default App;
