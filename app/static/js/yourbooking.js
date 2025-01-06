$(document).ready(function () {
  // Form submission handler
  $(".booking-btn").click(function () {
    // Validate required fields
    var datein = $("#date-in").val();
    var dateout = $("#date-out").val();
    var guest = $("#guest").val();
    var room = $("#room").val();

    if (!datein || !dateout || !guest || !room) {
      alert("Vui lòng điền đầy đủ thông tin trước khi tiếp tục!");
      return;
    } else {
      // Nếu tất cả trường hợp lệ, chuyển hướng đến trang đặt phòng
      var bookingUrl = $(this).data("url");
      window.location.href = bookingUrl;
    }
  });
});
