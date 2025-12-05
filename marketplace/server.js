const express = require("express");
const app = express();
app.use(express.json());
app.use(express.static("public"));

app.post("/api/preorder", (req, res) => {
  console.log("received preorder:", req.body);
  res.json({ ok: true, message: "Reservation saved (demo)" });
});

app.listen(3000, () => console.log("Server running on 3000"));
