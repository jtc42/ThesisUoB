$hashes = git rev-list --all
$outfile = "../wordcount.txt"

Clear-Content $outfile 

ForEach ($hash in $hashes)
{
    echo "Operating on hash: " $hash
    echo "Checking out..."
    git checkout $hash

    echo "Word-counting..."
    <# Get full wordcount.pl output #> 
    $countfull = texcount main.tex -inc -total

    <# Pull out the second line (index 1) containing word count #> 
    $countline = $countfull | Select -Index 1

    <# Pull out the number, stripping text #> 
    $n = $countline.Substring($countline.IndexOf(':')+2) -replace '(?:\r|\n)',''
    echo $n

    <# Get datetime of commit #>
    $dateline = git log -2 --pretty=tformat:%aD | Select -Index 0
    echo "DATELINE: " $dateline
    $datetime = $dateline -replace '(?:\r|\n)',''
    echo $datetime

    $outline = $datetime + "; " + $n

    echo $outline | Out-File -Append $outfile -Encoding ASCII
}

<# Revert back to latest #> 
git checkout master