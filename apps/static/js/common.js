$(document).ready(function () {

    $(function () {
        $(".alert").delay(2000).slideUp(300);
    });

    // счётчик количества товара на странице товара //
    $('.minus').click(function () {
        var $input = $(this).parent().find('input');
        var count = parseInt($input.val()) - 1;
        count = count < 1 ? 1 : count;
        $input.val(count);
        $input.change();
        return false;
    });
    $('.plus').click(function () {
        var $input = $(this).parent().find('input');
        $input.val(parseInt($input.val()) + 1);
        $input.change();
        return false;
    });
    // /счётчик количества товара на странице товара //

    // подсчёт стоимости товара с учётом количества на странице товара //
    $("#id_quantity").on("change", function (e) {
        $("span.total_price").text(+this.value * +$("span.price").text());
    });
    // /подсчёт стоимости товара с учётом количества на странице товара //

    // слайдер на главной странице, топ товаров //
    // https://github.com/ganlanyuan/tiny-slider
    var slider = tns({
        container: '.slider-index',
        items: 1,
        mouseDrag: true,
        nav: true,
        controls: true,
        slideBy: 'page',
        gutter: 0,
        // swipeAngle: false,
        navPosition: 'bottom',
        controlsPosition: 'bottom',
        controlsText: ["<i class=\"bi bi-chevron-left\"></i>", "<i class=\"bi bi-chevron-right\"></i>"],
        loop: false,
        // lazyload: true,
        responsive: {
            300: {
                edgePadding: 20,
                gutter: 25,
                items: 1
            },
            640: {
                edgePadding: 20,
                gutter: 20,
                items: 2
            },
            700: {
                gutter: 30,
                items: 3
            },
            900: {
                items: 4
            }
        }
    });
    // /слайдер на главной странице, топ товаров //


});


// пагинация //
function ajaxPagination() {
    $('.content a.page-link').each((index, el) => {
        $(el).click((e) => {
            e.preventDefault()
            let page_url = $(el).attr('href')

            $.ajax({
                url: page_url,
                type: 'GET',
                success: (data) => {
                    $('.content').empty()
                    $('.content').append($(data).find('.content').html())
                    $('html, body').animate({scrollTop: $(".content").offset().top}, 0);
                }
            })
        })
    })
}

$(document).ready(function () {
    ajaxPagination()
})

$(document).ajaxStop(function () {
    ajaxPagination()
})
// /пагинация //
