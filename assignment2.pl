my %hash = (
    'apple'  => 'red', # settting each key equal to said value
    'banana' => 'yellow',# key banana is set equal to yellow
    'pear'   => 'green',
);
while( my( $key, $value ) = each %hash ){ # does loop for each key value in each hash
    print "A(n) $key is $value\n"; #prints out the sentence and puts in each key in where $key is and each value in for $value.
#starts a new line for each pass of the loop.
}