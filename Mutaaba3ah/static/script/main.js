/* global variables */
var DATE_FORMAT = "dd M yy";

function toggleButtonSave() {
    var status = $('#isLoggedin').val();
    var btnSave = $('#btnSave');
    if (status == 'True') {
        btnSave.prop('disabled', false);
        btnSave.removeClass('button');
        btnSave.addClass('button-primary');
    } else {
        btnSave.prop('disabled', true);
        btnSave.removeClass('button-primary');
        btnSave.addClass('button');
    }
}

function setupTooltips() {
    $('#tilawah_to').qtip({
        content: 'Isi dengan halaman akhir tilawah. Atau isi dengan nomor Juz (kosongkan "halaman awal", jika kolom ini diisi no Juz).',
        position: {
            my: 'center left',
            at: 'center right'
        },
        show: {
            event: 'focus',
            effect: function () {
                $(this).show('slide', 500);
            }
        },
        hide: {
            event: 'blur',
            effect: function () {
                $(this).hide('slide', 500);
            }
        }
    });
}

function setupDatepickers() {
    $(function () {
        var currentDate = new Date();
        $("#tanggal").datepicker({
            dateFormat: DATE_FORMAT,
            onSelect: function () {
                var hidden = $('#tanggal_value');
                var date = $.datepicker.parseDate(DATE_FORMAT, $(this).val());
                hidden.val(date);
            }
        });
        $("#tanggal").datepicker("setDate", currentDate);
    })
}

function disableNonNumeric() {
    //http://stackoverflow.com/questions/995183/how-to-allow-only-numeric-0-9-in-html-inputbox-using-jquery
    $('input[type=number]').keydown(function (e) {
        // Allow: backspace, delete, tab, escape, enter and .
        if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110, 190]) !== -1 ||
            // Allow: Ctrl+A, Command+A
            (e.keyCode == 65 && (e.ctrlKey === true || e.metaKey === true)) ||
            // Allow: home, end, left, right, down, up
            (e.keyCode >= 35 && e.keyCode <= 40)) {
            // let it happen, don't do anything
            return;
        }
        // Ensure that it is a number and stop the keypress
        if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
            e.preventDefault();
        }
    });
}

function getPagesFromJuz(juz) {
    var start_page = 0;
    var end_page = 604;
    if (juz > 1) {
        start_page = (juz - 1) * 20 + 2;
    }
    if (juz != 30) {
        end_page = juz * 20 + 1
    }
    return {
        'halaman_awal': start_page,
        'halaman_akhir': end_page
    };
}

function showPagesCount() {
    var tilawah = $('#tilawah');
    var tilawah_to = $('#tilawah_to');
    var txtCount = $('#count');

    var halaman_awal = parseInt(tilawah.val());
    var halaman_akhir = parseInt(tilawah_to.val());

    if (halaman_awal) {
        if (halaman_akhir) {
            //jika halaman awal & halaman akhir diisi
            var jumlah = calculateTotalPages(halaman_awal, halaman_akhir);
            txtCount.val(jumlah);
        }
        else {
            //jika halaman akhir tidak diisi, set halaman akhir = halaman awal
            tilawah_to.val(halaman_awal);
            txtCount.val(1);
        }
    }
        //jika halaman awal tidak diisi, maka isian halaman akhir dianggap nomor Juz
    else {
        //validasi Juz
        if (halaman_akhir && halaman_akhir <= 30) {
            var pages = getPagesFromJuz(halaman_akhir);
            tilawah.val(pages.halaman_awal);
            tilawah_to.val(pages.halaman_akhir);
            var jumlah = calculateTotalPages(pages.halaman_awal, pages.halaman_akhir);
            txtCount.val(jumlah);
        }
        else {
            //validation error: isian Juz tidak valid
            $('<div><p>Nomor Juz harus berada di range 1-30. Jika Anda bermaksud mengisi nomor Halaman, maka pastikan "halaman awal" juga diisi.</p></div>').dialog({
                title: 'Isian Juz tidak valid'
            });
        }
    }
}

function validateForm() {
    if (!$('#tanggal').val()) {
        return false;
    }
    if ($('#tilawah').val() && $('#tilawah_to').val() && $('#count').val()) {
        return true;
    }
    if ($('#dhuha').val()) {
        return true;
    }
    if ($('#ql').val()) {
        return true;
    }
    if ($('input[type=radio][name=shaum]:selected').val()) {
        return true;
    }
}

function updateJsonformData() {
    //var jsonData = $('#form_laporan').serializeObject();
    //jsonData.tanggalConverted = $.datepicker.parseDate(DATE_FORMAT, jsonData.tanggal);
    //$('#formData').val(JSON.stringify(jsonData));
    var obj = $('#form_laporan').serializeObject();
    obj.formData = undefined;
    $('#formData').val(JSON.stringify(obj));
}

$(document).ready(function () {
    //enable-disable button Save according to user login status
    toggleButtonSave();
    
    //setup tooltip utk isian 'halaman akhir atau Juz'
    setupTooltips();

    //setup datepicker, default date : today
    setupDatepickers();

    //disable non-numeric input
    disableNonNumeric();

    //hitung jumlah halaman
    $('#tilawah').blur(function () {
        showPagesCount()
    });
    $('#tilawah_to').blur(function () {
        showPagesCount()
    });

    //jika dipanggi setelah submit, tampilkan dialog "berhasil save"
    if ($('#isSuccess').val() == true) {
        $('#formSucessDialog').dialog();
    }
    
    //validasi form saat submit: tanggal harus diisi dan minimal salah satu field terisi
    $("#form_laporan").submit(function (event) {
        var isValid = validateForm();
        if (!isValid) {
            $('#formInvalidDialog').dialog();
            event.preventDefault();
        }
        updateJsonformData();
    });
});