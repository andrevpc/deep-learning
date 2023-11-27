string path = args[0];
string destiny = args[1];

// path = ".\\folders";            
// destiny = ".\\folders\\train"; //!formato de destino a ser inserido 

string[] directories = Directory.GetDirectories(path);
try
{
    foreach (var dirPath in directories)
    {  
        System.Console.WriteLine("============================================");

        if (dirPath == destiny)
        {
            System.Console.WriteLine($"Destiny == {destiny}");
            continue;
        }
        var folder = Directory.GetDirectories(dirPath);
        foreach (var @class in folder)
        {
            var classes = @class.Split("\\");
            string ActClass = classes[classes.Length - 1];
            foreach (var file in Directory.GetFiles(@class))
            {
                var copySplit = file.Split("\\");
                string copy = copySplit[copySplit.Length - 1];
                File.Copy(file, $"{destiny}\\{ActClass}\\{copy}");
                System.Console.WriteLine(copy);
            }
        }
    }
}
catch (System.Exception e)
{
    System.Console.WriteLine(e.Message);
    throw;
}