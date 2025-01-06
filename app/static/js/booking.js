$(document).ready(function() {
    // Form submission handler
    $(".submit-btn").click(function() {
        // Validate required fields
        var name = $("#name").val();
        var email = $("#email").val();
        var phone = $("#phone").val();
        var countryCode = $("#country-code").val();
        var voucher = $("input[name='voucher']:checked").val();
        
        if (!name || !email || !phone || !voucher) {
            alert("Vui lòng điền đầy đủ thông tin trước khi tiếp tục!");
            return;
        }

        // Get selected services
        var services = [];
        $(".checkbox-item input[type='checkbox']:checked").each(function() {
            services.push($(this).siblings("label").text());
        });

        // Update summary modal
        var summaryHtml = `
            <p><strong>Họ và tên:</strong> ${name}</p>
            <p><strong>Email:</strong> ${email}</p>
            <p><strong>Số điện thoại:</strong> ${countryCode} ${phone}</p>
            <p><strong>Loại voucher:</strong> ${voucher === "self-use" ? "Tôi sử dụng" : "Tôi đặt cho người khác"}</p>
            <p><strong>Dịch vụ đã chọn:</strong> ${services.length > 0 ? services.join(", ") : "Không có"}</p>
        `;
        $("#booking-summary").html(summaryHtml);
        $("#summary-modal").modal("show");
    });

    // Modal navigation
    $("#continue-payment").click(function() {
        $("#summary-modal").modal("hide");
        $("#payment-modal").modal("show");
    });

    // Payment confirmation
    $("#confirm-payment").click(function() {
        var paymentMethod = $("input[name='payment_method']:checked").val();
        if (!paymentMethod) {
            alert("Vui lòng chọn phương thức thanh toán!");
            return;
        }
        // Submit form
        $("#booking-form").submit();
    });
});