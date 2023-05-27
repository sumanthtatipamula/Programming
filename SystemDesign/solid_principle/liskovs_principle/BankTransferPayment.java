package solid_principle.liskovs_principle;

public class BankTransferPayment implements PaymentMethod {
    private String accountNumber;
    private String bankCode;

    public BankTransferPayment(String accountNumber, String bankCode) {
        this.accountNumber = accountNumber;
        this.bankCode = bankCode;
    }

    @Override
    public void processPayment(double amount) {
        // Logic to process payment via bank transfer
        System.out.println("Processing bank transfer payment of $" + amount);
        // Additional implementation specific to bank transfers
        // ...
    }
}