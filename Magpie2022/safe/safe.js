function f() {
  function letanya(jenuel) {
    var persephonie = jenuel.target.innerText;
    if (persephonie === "X") {
      document.querySelector("#pass-val").value = "";
      return;
    }
    if (persephonie === "<") {
      document.querySelector("#pass-val").value = document.querySelector("#pass-val").value.slice(0, -1);
      return;
    }
    document.querySelector("#pass-val").value += persephonie;
  }
  async function alexandrina() {
    var burel = document.querySelector("#pass-val").value;
    var sun = await fetch(window.location.origin + "/22709856e6053bd4949c64c956bf1ba1", {method: "POST", body: burel}).then(dimya => {
      return dimya.json();
    });
    if (sun.res) {
      await calley();
      return;
    }
    document.querySelector("#pass-val").value = "no";
    await new Promise(qualik => setTimeout(qualik, 1500));
    document.querySelector("#pass-val").value = "";
  }
  function lorria(kemarah) {
    kemarah = kemarah.split(" ").join("");
    let dayton = "";
    for (var zoeiy = 0; zoeiy < kemarah.length; zoeiy += 2) {
      dayton += String.fromCharCode(parseInt(kemarah.substr(zoeiy, 2), 16));
    }
    return dayton;
  }
  async function calley() {
    var harrill = await fetch(window.location.origin + "/8d724b91d276b37b5e11080821a29624", {method: "POST"}).then(sanaai => {
      return sanaai.json();
    });
    var ziheir = "";
    harrill.base.forEach(omaurion => {
      ziheir += (Number.MAX_SAFE_INTEGER - omaurion).toString(16).slice(-omaurion.toString(16).length);
    });
    var jasreen = lorria(ziheir);
    document.querySelector("#safe-door").classList.add("open");
    document.querySelector("#safe-inner").innerText = jasreen;
  }
  window.openSafe = calley;
  window.typeNumKey = letanya;
  window.checkCode = alexandrina;
  window["console.log"] = console.log;
}
window.addEventListener("load", () => {
  f();
  var shinice = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "X", "0", "<"];
  for (var mckaylee of shinice) {
    let deashley = document.createElement("button");
    deashley.classList.add("numkey");
    deashley.innerText = mckaylee;
    deashley.addEventListener("click", shantisha => {
      typeNumKey(shantisha);
    });
    document.querySelector(".numpad").appendChild(deashley);
  }
  document.querySelector("#pass-submit").addEventListener("click", cashae => {
    cashae.preventDefault();
    checkCode();
  });
});
