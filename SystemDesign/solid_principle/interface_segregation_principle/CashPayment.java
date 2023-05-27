package solid_principle.interface_segregation_principle;

public class CashPayment implements OfflinePayment {
    public void processOfflinePayment() {
        // Process cash payment offline
    }
}
