$(document).ready(function() {
    // Apply voucher handler
    $('#apply-voucher').click(function() {
        $.ajax({
            url: '/promotion/', // URL đến trang promotion.html
            type: 'GET',
            success: function(data) {
                // Lấy danh sách các voucher từ dữ liệu trả về
                var voucherList = $(data).find('.promotion-item');

                // Xóa danh sách voucher cũ
                $('#voucher-list-container').empty();

                // Thêm từng voucher vào modal
                voucherList.each(function() {
                    var voucher = $(this);
                    var voucherId = voucher.attr('id'); // Lấy ID của voucher
                    var voucherCode = voucher.find('h6').text(); // Lấy mã voucher
                    var voucherDiscount = voucher.find('h5').text(); // Lấy phần trăm giảm giá

                    // Tạo nút voucher với mã voucher và phần trăm giảm giá
                    var voucherButton = $('<button type="button" class="btn btn-outline-primary">' + voucherCode + ' - ' + voucherDiscount + '</button>');

                    // Thêm sự kiện click cho nút voucher
                    voucherButton.click(function() {
                        // Áp dụng mã voucher vào input
                        $('#voucher-code').val(voucherCode);

                        // Tính toán giá trị giảm giá 
                        var totalPrice = parseFloat($('#total-price').text().replace(/\./g, '').replace(' VNĐ', '')); // Lấy tổng giá tiền và chuyển đổi sang số
                        var discountPercentage = parseFloat(voucherDiscount.replace('Giảm ', '').replace('%', '')); // Lấy phần trăm giảm giá và chuyển đổi sang số
                        var discountAmount = totalPrice * (discountPercentage / 100); // Tính giá trị giảm giá
                        
                        // Hiển thị số tiền giảm
                        $('#discount-amount').text('Voucher: ' + -(discountAmount.toLocaleString('vi-VN')) + ' VNĐ'); 

                        // Tính và hiển thị "Thành tiền"
                        var finalPrice = totalPrice - discountAmount; // Tính tổng giá tiền sau khi giảm giá
                        $('#final-price').text('Thành tiền: ' + finalPrice.toLocaleString('vi-VN') + ' VNĐ'); 

                        // Ẩn modal
                        $('#voucherModal').modal('hide');
                    });

                    // Thêm nút voucher vào danh sách
                    $('#voucher-list-container').append(voucherButton);
                });
            }
        });
    });

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