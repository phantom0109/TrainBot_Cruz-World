<processors>
  <processor name="Extract Attributes from Alias">
    <type>org.apache.nifi.processors.standard.EvaluateRegex</type>
    <properties>
      <property name="Regular Expression">^(.*?)_(.*?)_(.*?)$</property>
      <property name="Group Names">partA,partB,partC</property>
      <property name="Destination">flowfile-attribute</property>
      <property name="Attribute Name">alias</property>
    </properties>
  </processor>
</processors>

Scribe AI
To add attributes to the JSON content in a flow file based upon RegEx matches of another attribute already in the flow file, you can use the UpdateAttribute processor within Apache Nifi.

Here are the steps to configure this processor:

Drag and drop an UpdateAttribute processor onto your canvas.

Connect it to your input source.

In the properties panel for UpdateAttribute, click on "Add" button under "User-defined Properties".

Enter a name for your new property (e.g., partA) and then enter an expression that uses Regular Expression Language (RegEx) to extract the desired value from your existing attribute using capture groups.

For example, if you want to extract partA from alias attribute, you could use this expression: ${alias:replaceAll('^(\\w{8})_(\\w{8})_(C\\d+)$','$1')}

This will create a new attribute called "partA" with its value extracted from alias using RegEx pattern matching.

Repeat step 4 for each additional attribute that needs to be added based on RegEx matches of other attributes in the flow file.

Save and run your workflow.

With these steps, when data is passed through this pipeline, it will have additional attributes added based on regular expressions applied against existing attributes in each FlowFile's JSON content as per requirement mentioned above.