import _plotly_utils.basevalidators


class BordercolorValidator(_plotly_utils.basevalidators.ColorValidator):

    def __init__(
        self, plotly_name='bordercolor', parent_name='layout.legend', **kwargs
    ):
        super(BordercolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='legend',
            role='style',
            **kwargs
        )