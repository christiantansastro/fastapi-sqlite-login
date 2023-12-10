const sqlite3 = require("sqlite3").verbose();
const db = new sqlite3.Database("users.db");

db.serialize(() => {
  db.run(
    "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)"
  );

  db.run(
    `INSERT INTO users (username, password) VALUES ('chris', 'sqlite')`,
    function (err) {
      if (err) {
        return console.log(err.message);
      }
      // get the last insert id
      console.log(`A row has been inserted with rowid ${this.lastID}`);
    }
  );

  db.close();
});
