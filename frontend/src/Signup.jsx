import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Signup() {
// 시간 지날수록 바꿀수 있는 것들 마지막 업데이트로 되어있는걸 볼수있게함
  const [username, setUsername] = useState("");
  const [englishName, setEnglishName] = useState("");
  const [usPhoneNumber, setUsPhoneNumber] = useState("");
  const [email, setEmail] = useState("");
  const [gender, setGender] = useState("");
  const [birthDate, setBirthDate] = useState("");
  const [school, setSchool] = useState("");
  const [gradDate, setGradDate] = useState("");
  const [role, setRole] = useState("user");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent form from refreshing the page on submit

    // user is an object that holds all the state varible and try to send all of those to the backend instead of sending one by one
    const user = {
      username,
      english_name: englishName,
      us_phone_number: usPhoneNumber,
      email,
      gender,
      birth_date: birthDate,
      school,
      grad_date: gradDate,
      role,
      password,
      
    };

    try {
      // Try to send the user object to the backend
      const response = await axios.post("http://localhost:8000/signup/", user);
      
      // successful then go to the login page
      navigate("/login");

      // successful
      console.log("우리의 동료가 된걸 축하한다",response.data.message);
    } catch (error) {
      // Failed
      console.error("안타깝지만 동료는 되지 못할거같다 다시 입력해라", error.response.data);
    }
  };

  return (
    <div>
      <h2>얼른 회원가입이나 해라
      </h2>
      <form onSubmit={handleSubmit}>
        <label>
          Username:
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)} 
          />
        </label>
        <br />
        <label>
          English Name:
          <input
            type="text"
            value={englishName}
            onChange={(e) => setEnglishName(e.target.value)}
          />
        </label>
        <br />
        <label>
          US Phone Number:
          <input
            type="text"
            value={usPhoneNumber}
            onChange={(e) => setUsPhoneNumber(e.target.value)}
          />
        </label>
        <br />
        <label>
          Email:
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </label>
        <br />
        <label>
          Gender:
          <select
            value={gender}
            onChange={(e) => setGender(e.target.value)}
          >
            <option value="">Select Gender</option>
            <option value="M">Male</option>
            <option value="F">Female</option>
          </select>
        </label>
        <br />
        <label>
          Birth Date:
          <input
            type="date"
            value={birthDate}
            onChange={(e) => setBirthDate(e.target.value)}
          />
        </label>
        <br />
        <label>
          School:
          <input
            type="text"
            value={school}
            onChange={(e) => setSchool(e.target.value)}
          />
        </label>
        <br />
        <label>
          Graduation Date:
          <input
            type="number"
            value={gradDate}
            onChange={(e) => setGradDate(e.target.value)}
          />
        </label>
        <br />
        <label>
          Role:
          <select
            value={role}
            onChange={(e) => setRole(e.target.value)}
          >
            <option value="user">User</option>
            <option value="admin">Admin</option>
          </select>
        </label>
        <br />

        <label>
          Password:
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)} 
          />
        </label>
        
        <br />
        <button type="submit">동료가 되겠습니까?</button>
      </form>
    </div>
  );
}

export default Signup;
