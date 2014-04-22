YUI({
    classNamePrefix: 'pure'
}).use('gallery-sm-menu', function (Y) {

    var horizontalMenu = new Y.Menu({
        container         : '#demo-horizontal-menu',
        sourceNode        : '#menu',
        orientation       : 'horizontal',
        hideOnOutsideClick: false,
        hideOnClick       : false
    });

    horizontalMenu.render();
    horizontalMenu.show();

});