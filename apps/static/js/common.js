$(document).ready(function () {
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

    // слайдер на главной странице, топ товаров
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
        controlsText: ["<i class=\"bi bi-arrow-left\"></i>", "<i class=\"bi bi-arrow-right\"></i>"],
        loop: false,
        // lazyload: true,
        responsive: {
            300: {
                edgePadding: 20,
                gutter: 20,
                items: 2
            },
            640: {
                edgePadding: 20,
                gutter: 20,
                items: 3
            },
            700: {
                gutter: 30,
                items: 4
            },
            900: {
                items: 5
            }
        }
    });

});