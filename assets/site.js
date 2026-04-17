(() => {
  const mobileToggle = document.querySelector("[data-mobile-toggle]");
  const siteNav = document.getElementById("site-nav");

  if (mobileToggle && siteNav) {
    mobileToggle.addEventListener("click", () => {
      const isOpen = siteNav.classList.toggle("is-open");
      mobileToggle.setAttribute("aria-expanded", String(isOpen));
    });
  }

  // ── Lightbox ───────────────────────────────────────────
  const overlay = document.createElement("div");
  overlay.className = "lightbox-overlay";
  overlay.setAttribute("role", "dialog");
  overlay.setAttribute("aria-label", "Image viewer");
  overlay.innerHTML = '<button class="lightbox-close" aria-label="Close image viewer">&times;</button><img src="" alt="">';
  document.body.appendChild(overlay);

  const lightboxImg = overlay.querySelector("img");
  const closeBtn = overlay.querySelector(".lightbox-close");

  const openLightbox = (src, alt) => {
    lightboxImg.src = src;
    lightboxImg.alt = alt || "";
    overlay.classList.add("is-open");
    document.body.style.overflow = "hidden";
  };

  const closeLightbox = () => {
    overlay.classList.remove("is-open");
    document.body.style.overflow = "";
    setTimeout(() => { lightboxImg.src = ""; }, 200);
  };

  // Click on images to open lightbox
  document.addEventListener("click", (e) => {
    const img = e.target.closest("img");
    if (img && img.src && !img.closest(".lightbox-overlay")) {
      openLightbox(img.src, img.alt);
    }
  });

  // Close on button click
  closeBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    closeLightbox();
  });

  // Close on backdrop click
  overlay.addEventListener("click", (e) => {
    if (e.target === overlay) closeLightbox();
  });

  // Close on Escape
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && overlay.classList.contains("is-open")) closeLightbox();
  });
})();
