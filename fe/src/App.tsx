import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [count, setCount] = useState<number>(0);
  const apiUrl = process.env.REACT_APP_API_URL;

  useEffect(() => {
    fetchCount();
  }, []);

  const fetchCount = async () => {
    try {
      const response = await axios.get(`${apiUrl}/counter`);
      setCount(response.data.count);
    } catch (error) {
      console.error("숫자 가져오기 실패", error);
    }
  };

  const incrementCount = async () => {
    try {
      const response = await axios.post(`${apiUrl}/counter/increment`);
      setCount(response.data.count);
    } catch (error) {
      console.error("숫자 증가 실패:", error);
    }
  };

  const decrementCount = async () => {
    try {
      const response = await axios.post(`${apiUrl}/counter/decrement`);
      setCount(response.data.count);
    } catch (error) {
      console.error("숫자 감소 실패:", error);
    }
  };

  return (
    <div className="App">
      <h1>현재숫자: {count}</h1>
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "space-evenly",
        }}
      >
        <button onClick={incrementCount}>증가</button>
        <button onClick={decrementCount}>감소</button>
      </div>
    </div>
  );
}

export default App;
