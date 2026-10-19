// Swap this for the Sell.app (or other) checkout URL when ready. Leave "" to show "coming soon".
const CARD_CHECKOUT_URL = "";
const SOL_ADDRESS = "EKNpkRpGss6Y3NdopdDRs91EiTemEVGNUFXR3Bzif2AN";
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-card-checkout]").forEach(b => {
    if (CARD_CHECKOUT_URL) { b.href = CARD_CHECKOUT_URL; b.textContent = "Buy with card"; b.removeAttribute("aria-disabled"); }
    else b.addEventListener("click", e => e.preventDefault());
  });
  document.querySelectorAll("[data-copy]").forEach(b => b.addEventListener("click", async () => {
    try { await navigator.clipboard.writeText(SOL_ADDRESS); }
    catch { const t = document.createElement("textarea"); t.value = SOL_ADDRESS; document.body.appendChild(t); t.select(); document.execCommand("copy"); t.remove(); }
    const o = b.textContent; b.textContent = "Copied!"; setTimeout(() => b.textContent = o, 1500);
  }));
});
