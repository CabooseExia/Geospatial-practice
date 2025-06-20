import { useState, useEffect } from "react";
import Login from "./Login";
import Home from "./Home";

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch("/api/user", { credentials: "include" })
      .then(res => res.ok ? res.json() : { authenticated: false })
      .then(data => {
        if (data.authenticated) setUser(data.username);
      });
  }, []);

  return (
    <>
      {user ? <Home user={user} setUser={setUser} /> : <Login setUser={setUser} />}
    </>
  );
}

export default App;
