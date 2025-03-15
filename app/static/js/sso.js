class SSO {
  constructor(options = {}) {
    this.loginUrl = options.loginUrl || "https://example.com/sso/login";
    this.width = options.width || 600;
    this.height = options.height || 700;
    this.validateEndpoint = options.validateEndpoint || "/auth/validate";
    this.redirectUrl = options.redirectUrl || "/";

    // Nasłuchiwanie wiadomości z okna SSO
    window.addEventListener("message", this.handleMessage.bind(this));
  }

  openLoginWindow() {
    const left = (window.innerWidth - this.width) / 2;
    const top = (window.innerHeight - this.height) / 2;
    const features = `width=${this.width},height=${this.height},left=${left},top=${top}`;

    this.loginWindow = window.open(this.loginUrl, "SSOLogin", features);

    if (!this.loginWindow) {
      alert("Proszę zezwolić na wyskakujące okienka dla tej strony.");
    }
  }

  async handleMessage(event) {
    // Sprawdzenie czy wiadomość pochodzi z oczekiwanego źródła
    if (event.origin !== new URL(this.loginUrl).origin) {
      return;
    }

    const data = event.data;

    if (data && data.status === "success" && data.token) {
      // Zamknięcie okna logowania
      if (this.loginWindow) {
        this.loginWindow.close();
      }

      try {
        // Wysłanie tokenu do walidacji
        const response = await fetch(this.validateEndpoint, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ token: data.token }),
        });

        const result = await response.json();

        if (result.success) {
          // Przekierowanie do strony głównej po udanym logowaniu
          window.location.href = this.redirectUrl;
        } else {
          alert("Błąd logowania: " + (result.error || "Nieznany błąd"));
        }
      } catch (error) {
        console.error("Błąd podczas walidacji tokenu:", error);
        alert("Wystąpił błąd podczas logowania. Spróbuj ponownie.");
      }
    }
  }
}
