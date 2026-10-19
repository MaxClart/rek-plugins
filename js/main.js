const SOL_ADDRESS = "EKNpkRpGss6Y3NdopdDRs91EiTemEVGNUFXR3Bzif2AN";
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-copy]").forEach(b => b.addEventListener("click", async () => {
    try { await navigator.clipboard.writeText(SOL_ADDRESS); }
    catch { const t = document.createElement("textarea"); t.value = SOL_ADDRESS; document.body.appendChild(t); t.select(); document.execCommand("copy"); t.remove(); }
    const o = b.textContent; b.textContent = "Copied!"; setTimeout(() => b.textContent = o, 1500);
  }));
});
