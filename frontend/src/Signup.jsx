import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Signup() {
// 시간 지날수록 바꿀수 있는 것들 마지막 업데이트로 되어있는걸 볼수있게함
  const [username, setUsername] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [usPhoneNumber, setUsPhoneNumber] = useState("");
  const [email, setEmail] = useState("");
  const [gender, setGender] = useState("");
  const [birthDate, setBirthDate] = useState("");
  const [gradDate, setGradDate] = useState("");
  const [password, setPassword] = useState("");
  const [major, setMajor] = useState("");
  const [error, setError] = useState(null);

  const navigate = useNavigate();

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent form from refreshing the page on submit
    // user is an object that holds all the state varible and try to send all of those to the backend instead of sending one by one
    const user = {
      username,
      first_name: firstName,
      last_name:lastName,
      us_phone_number: usPhoneNumber,
      email,
      gender,
      birth_date: birthDate,
      grad_date: gradDate,
      major,
      password,

    };
    console.log("Sending Sighnup Request: ", user);
    // Log the request before sending
    try {
        // ✅ Step 1: Signup the user
        await axios.post("http://localhost:8000/signup/", user);
        console.log("🎉 동료가 된걸 축하한다!");
        navigate("/");
    }
    catch(error){
      console.error("회원가입 실패", error.response?.data);
      setError(error.response?.data || "회원가입 실패")

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
          First Name:
          <input
            type="text"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
          />
        </label>
        <br/>
        <label>
          Last Name:
          <input
            type="text"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
          />
        </label>
        <br />
        <label>
          US Phone Number:
          <input
            type="tel"
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
            required
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
            required
          />
        </label>
        <br />
        <label>
          Graduation Date:
          <input
            type="number"
            value={gradDate}
            onChange={(e) => setGradDate(e.target.value)}
            required
          />
        </label>
        <br />
        <label>
          Major:
          <input
            type="text"
            value={major}
            onChange={(e) => setMajor(e.target.value)} 
          />
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
