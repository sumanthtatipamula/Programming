package solid_principle.interface_segregation_principle;

public class BankTransferPayment implements OnlinePayment, OfflinePayment {
    public void processOnlinePayment() {
        // Process bank transfer payment online
    }

    public void processOfflinePayment() {
        // Process bank transfer payment offline
    }
}