import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"
import Plot from 'react-plotly.js';

class StreamlitPlotlyEventsComponent extends StreamlitComponentBase {
  public render = (): ReactNode => {
    
    console.log(this.props.args["override_width"])
    
    // Pull Plotly object from args and parse
    const plot_obj = JSON.parse(this.props.args["plot_obj"]);
    const override_height = this.props.args["override_height"];
    let height = override_height ? override_height : plot_obj.layout.height;

    // Set width based on use_container width or provided with if not overriden by user
    const use_container_width = this.props.args["use_container_width"];
    const override_width = this.props.args["override_width"];
    let width = override_width ? override_width : this.props.width;
    width = use_container_width ? this.props.width : override_width;


    // Make the actual plotly chart size responsive if desired
    plot_obj.layout.width = width;
    plot_obj.layout.height = height;
    plot_obj.layout.autoresize = true;

    // Event booleans
    const click_event = this.props.args["click_event"];
    const select_event = this.props.args["select_event"];
    const hover_event = this.props.args["hover_event"];

    // Streamlit sends us a theme object via props that we can use to ensure
    // that our component has visuals that match the active theme in a
    // streamlit app but we won't use it for now.
    //const { theme } = this.props
    const style: React.CSSProperties = {
      width: '100%',
      height: '100%',
      overflowX: 'auto',
      overflowY: 'hidden',
    }

    Streamlit.setFrameHeight(override_height);
    return (
      <Plot
        data={plot_obj.data}
        layout={plot_obj.layout}
        config={plot_obj.config}
        frames={plot_obj.frames}
        onClick={click_event ? this.plotlyEventHandler : function(){}}
        onSelected={select_event ? this.plotlyEventHandler : function(){}}
        onHover={hover_event ? this.plotlyEventHandler : function(){}}
        style={style}
        useResizeHandler={true}
        className="stPlotlyChart"
      />
    )
  }

  /** Click handler for plot. */
  private plotlyEventHandler = (data: any) => {
    // Build array of points to return
    var clickedPoints: Array<any> = [];
    data.points.forEach(function (arrayItem: any) {
      clickedPoints.push({
        x: arrayItem.x,
        y: arrayItem.y,
        curveNumber: arrayItem.curveNumber,
        pointNumber: arrayItem.pointNumber,
        pointIndex: arrayItem.pointIndex
      })
    });

    // Return array as JSON to Streamlit
    Streamlit.setComponentValue(JSON.stringify(clickedPoints))
  }
}

export default withStreamlitConnection(StreamlitPlotlyEventsComponent)
