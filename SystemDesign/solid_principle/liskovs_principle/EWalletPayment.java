package solid_principle.liskovs_principle;

public class EWalletPayment implements PaymentMethod {
    private String eWalletId;
    private String password;

    public EWalletPayment(String eWalletId, String password) {
        this.eWalletId = eWalletId;
        this.password = password;
    }

    @Override
    public void processPayment(double amount) {
        // Logic to process payment using e-wallet
        System.out.println("Processing e-wallet payment of $" + amount);
        // Additional implementation specific to e-wallet payments
        // ...
    }
}
