(function(){
  var slides = Array.prototype.slice.call(document.querySelectorAll(".slide"));
  function actual(){
    var y = window.scrollY + window.innerHeight * 0.35, idx = 0;
    slides.forEach(function(s, i){ if (s.offsetTop <= y) idx = i; });
    return idx;
  }
  function ir(i){
    i = Math.max(0, Math.min(slides.length - 1, i));
    var id = slides[i].id;
    history.replaceState(null, "", "#" + id);
    slides[i].scrollIntoView();
  }
  if (location.hash) {
    var destino = document.getElementById(location.hash.slice(1));
    if (destino) { document.documentElement.style.scrollBehavior = "auto"; destino.scrollIntoView(); setTimeout(function(){ document.documentElement.style.scrollBehavior = ""; }, 100); }
  }
  try { if (localStorage.getItem("proyeccion") === "1") document.documentElement.classList.add("proyeccion"); } catch(e){}
  document.addEventListener("keydown", function(e){
    if (e.altKey || e.ctrlKey || e.metaKey) return;
    var t = e.target.tagName;
    if (t === "INPUT" || t === "TEXTAREA") return;
    if (e.key === "ArrowRight" || e.key === "PageDown" || e.key === "ArrowDown" && e.shiftKey) { e.preventDefault(); ir(actual() + 1); }
    else if (e.key === "ArrowLeft" || e.key === "PageUp" || e.key === "ArrowUp" && e.shiftKey) { e.preventDefault(); ir(actual() - 1); }
    else if (e.key === "Home") { e.preventDefault(); ir(0); }
    else if (e.key === "p" || e.key === "P") {
      var i = actual();
      var on = document.documentElement.classList.toggle("proyeccion");
      try { localStorage.setItem("proyeccion", on ? "1" : "0"); } catch(e){}
      setTimeout(function(){ slides[i].scrollIntoView(); }, 50);
    }
    else if (e.key === "f" || e.key === "F") {
      if (!document.fullscreenElement) { document.documentElement.requestFullscreen && document.documentElement.requestFullscreen(); }
      else { document.exitFullscreen && document.exitFullscreen(); }
    }
  });
})();
