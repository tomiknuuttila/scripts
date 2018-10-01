var fs = require('fs');
 
if (process.argv.length <= 2) {
    console.log("Usage: " + __filename + " path/to/directory");
    process.exit(-1);
}
 
var path = process.argv[2];
 
fs.readdir(path, function(err, items) {

        for (var i=0; i<items.length; i++) {

            if(items[i].includes("html"))   {
                console.log(items[i]);
                console.log("\n");
                openFile(items[i]);
            }
        }
    }
);

function openFile(filename) {

    if(!filename)    {
        return;
    }

    var filepath = path + filename;

    rl = require('readline').createInterface({
        input: require('fs').createReadStream(filepath)
    });

   rl.on(
        'line',
        function(line)  {
            checkLine(line);
        }
    )

    console.log("\n");

    return;
}

function checkLine(line)    {

    if(line.includes("#T1"))    {
        console.log(line)
    }

    return;
}