(function () {
  "use strict";

  var canvas = document.getElementById("canvas");
  var zoomed = document.getElementById("zoomed");
  var zoomedImg = document.getElementById("zoomed-img");
  var zoomedCaption = document.getElementById("zoomed-caption");
  var zoomedInner = zoomed && zoomed.querySelector(".zoomed-inner");
  var backBtn = zoomed && zoomed.querySelector(".zoomed-back");

  function openZoom(src, alt, captionText) {
    if (!zoomed || !zoomedImg) return;
    zoomedImg.src = src;
    zoomedImg.alt = alt || "";
    zoomedCaption.textContent = captionText || "";
    zoomed.classList.remove("hidden");
    zoomed.setAttribute("aria-hidden", "false");
    if (canvas) canvas.classList.add("zoomed-out");
    document.body.style.overflow = "hidden";
  }

  function closeZoom() {
    if (!zoomed) return;
    zoomed.classList.add("hidden");
    zoomed.setAttribute("aria-hidden", "true");
    if (canvas) canvas.classList.remove("zoomed-out");
    document.body.style.overflow = "";
  }

  function handlePolaroidClick(e) {
    if (e.target.closest("a")) return;
    var polaroid = e.target.closest("[data-zoom]");
    if (!polaroid) return;
    var img = polaroid.querySelector("img");
    var cap = polaroid.querySelector("figcaption");
    if (!img) return;
    e.preventDefault();
    openZoom(img.src, img.alt, cap ? cap.textContent.trim() : "");
  }

  function handleZoomedClick(e) {
    if (e.target === zoomed || e.target === backBtn) closeZoom();
  }

  function handleZoomedInnerClick(e) {
    e.stopPropagation();
  }

  if (canvas) {
    canvas.addEventListener("click", handlePolaroidClick);
  }

  if (zoomed) {
    zoomed.addEventListener("click", handleZoomedClick);
    if (zoomedInner) zoomedInner.addEventListener("click", handleZoomedInnerClick);
  }

  if (backBtn) {
    backBtn.addEventListener("click", closeZoom);
  }

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && zoomed && !zoomed.classList.contains("hidden")) {
      closeZoom();
    }
  });
})();
